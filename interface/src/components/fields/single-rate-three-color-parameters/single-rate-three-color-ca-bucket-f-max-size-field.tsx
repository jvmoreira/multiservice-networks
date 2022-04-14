import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { SingleRateThreeColorParameterFieldProps } from './single-rate-three-color-parameters';

export function SingleRateThreeColorCaBucketFMaxSizeField(props: SingleRateThreeColorParameterFieldProps): ReactElement {
  const { singleRateThreeColorParameters, setSingleRateThreeColorParameters } = props;

  const singleRateThreeColorCaBucketFMaxSize = useMemo(() => {
    return singleRateThreeColorParameters.ca_bucketF_max_size || '';
  }, [singleRateThreeColorParameters]);

  const setSingleRateThreeColorCaBucketFMaxSize = useSetNfvTeFunctionParameter('ca_bucketF_max_size', setSingleRateThreeColorParameters);
  const onSingleRateThreeColorCaBucketFMaxSizeChangeHandler = useChangeHandler(setSingleRateThreeColorCaBucketFMaxSize);

  return (
    <FormInput
      label="Tamanho Máximo do Bucket C do Color Aware"
      name="ca-bucket-f-max-size"
      value={singleRateThreeColorCaBucketFMaxSize}
      placeholder="Valor em tokens"
      onChange={onSingleRateThreeColorCaBucketFMaxSizeChangeHandler}
    />
  );
}
