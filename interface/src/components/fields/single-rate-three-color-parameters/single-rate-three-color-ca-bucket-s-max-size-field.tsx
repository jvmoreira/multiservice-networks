import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { SingleRateThreeColorParameterFieldProps } from './single-rate-three-color-parameters';

export function SingleRateThreeColorCaBucketSMaxSizeField(props: SingleRateThreeColorParameterFieldProps): ReactElement {
  const { singleRateThreeColorParameters, setSingleRateThreeColorParameters } = props;

  const singleRateThreeColorCaBucketSMaxSize = useMemo(() => {
    return singleRateThreeColorParameters.ca_bucketS_max_size || '';
  }, [singleRateThreeColorParameters]);

  const setSingleRateThreeColorCaBucketSMaxSize = useSetNfvTeFunctionParameter('ca_bucketS_max_size', setSingleRateThreeColorParameters);
  const onSingleRateThreeColorCaBucketSMaxSizeChangeHandler = useChangeHandler(setSingleRateThreeColorCaBucketSMaxSize);

  return (
    <FormInput
      label="Tamanho Máximo do Bucket E do Color Aware"
      name="ca-bucket-s-max-size"
      value={singleRateThreeColorCaBucketSMaxSize}
      placeholder="Valor em tokens"
      onChange={onSingleRateThreeColorCaBucketSMaxSizeChangeHandler}
    />
  );
}
