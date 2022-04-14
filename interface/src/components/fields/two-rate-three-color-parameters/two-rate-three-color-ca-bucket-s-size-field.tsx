import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TwoRateThreeColorParameterFieldProps } from './two-rate-three-color-parameters';

export function TwoRateThreeColorCaBucketSSizeField(props: TwoRateThreeColorParameterFieldProps): ReactElement {
  const { twoRateThreeColorParameters, setTwoRateThreeColorParameters } = props;

  const twoRateThreeColorCaBucketSSize = useMemo(() => {
    return twoRateThreeColorParameters.ca_bucketS_size || '';
  }, [twoRateThreeColorParameters]);

  const setTwoRateThreeColorBucketSSize = useSetNfvTeFunctionParameter('ca_bucketS_size', setTwoRateThreeColorParameters);
  const onTwoRateThreeColorBucketSSizeChangeHandler = useChangeHandler(setTwoRateThreeColorBucketSSize);

  return (
    <FormInput
      label="Quantidade Inicial de Tokens no Bucket P do Color Aware"
      name="ca-bucket-s-size"
      value={twoRateThreeColorCaBucketSSize}
      onChange={onTwoRateThreeColorBucketSSizeChangeHandler}
    />
  );
}
